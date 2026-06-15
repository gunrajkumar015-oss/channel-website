// API Configuration
const API_BASE_URL = 'http://localhost:8000/api';
const TOKEN = localStorage.getItem('token');

// Initialize
document.addEventListener('DOMContentLoaded', function() {
    loadTrendingVideos();
    loadPopularChannels();
    checkAuthStatus();
});

// Authentication
function checkAuthStatus() {
    if (TOKEN) {
        document.getElementById('auth-menu').innerHTML = `
            <li class="nav-item dropdown">
                <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown">
                    <i class="fas fa-user"></i> Account
                </a>
                <ul class="dropdown-menu">
                    <li><a class="dropdown-item" href="pages/profile.html">Profile</a></li>
                    <li><a class="dropdown-item" href="pages/dashboard.html">Dashboard</a></li>
                    <li><hr class="dropdown-divider"></li>
                    <li><a class="dropdown-item" href="#" onclick="logout()">Logout</a></li>
                </ul>
            </li>
        `;
    }
}

function logout() {
    localStorage.removeItem('token');
    window.location.href = '../index.html';
}

// Load Videos
function loadTrendingVideos() {
    fetch(`${API_BASE_URL}/videos/?ordering=-views_count`)
    .then(response => response.json())
    .then(data => {
        const container = document.getElementById('trending-videos');
        if (container && data.results) {
            container.innerHTML = data.results.slice(0, 6).map(video => `
                <div class="col-md-6 col-lg-4">
                    <div class="card h-100 shadow-sm">
                        <img src="${video.thumbnail || 'https://via.placeholder.com/300x200'}" class="card-img-top" alt="${video.title}">
                        <div class="card-body">
                            <h5 class="card-title">${video.title}</h5>
                            <p class="card-text text-muted">${video.channel.name}</p>
                            <div class="d-flex justify-content-between">
                                <small><i class="fas fa-eye"></i> ${video.views_count} views</small>
                                <small><i class="fas fa-heart"></i> ${video.likes_count} likes</small>
                            </div>
                        </div>
                        <div class="card-footer bg-transparent border-0">
                            <a href="pages/video.html?id=${video.id}" class="btn btn-primary btn-sm w-100">Watch</a>
                        </div>
                    </div>
                </div>
            `).join('');
        }
    })
    .catch(error => console.error('Error loading videos:', error));
}

// Load Channels
function loadPopularChannels() {
    fetch(`${API_BASE_URL}/channels/?ordering=-subscribers_count`)
    .then(response => response.json())
    .then(data => {
        const container = document.getElementById('popular-channels');
        if (container && data.results) {
            container.innerHTML = data.results.slice(0, 4).map(channel => `
                <div class="col-md-6 col-lg-3">
                    <div class="card text-center shadow-sm">
                        <img src="${channel.profile_image || 'https://via.placeholder.com/150'}" class="card-img-top rounded-circle mt-3" alt="${channel.name}" width="150">
                        <div class="card-body">
                            <h5 class="card-title">${channel.name}</h5>
                            <p class="card-text text-muted">${channel.subscribers_count.toLocaleString()} subscribers</p>
                            <button class="btn btn-primary btn-sm" onclick="subscribe(${channel.id})">Subscribe</button>
                        </div>
                    </div>
                </div>
            `).join('');
        }
    })
    .catch(error => console.error('Error loading channels:', error));
}

// Subscribe to Channel
function subscribe(channelId) {
    if (!TOKEN) {
        window.location.href = 'pages/login.html';
        return;
    }
    
    fetch(`${API_BASE_URL}/channels/${channelId}/subscribe/`, {
        method: 'POST',
        headers: {
            'Authorization': `Token ${TOKEN}`,
            'Content-Type': 'application/json',
        }
    })
    .then(response => response.json())
    .then(data => {
        alert('Subscribed successfully!');
        loadPopularChannels();
    })
    .catch(error => console.error('Error:', error));
}

// Like Content
function likeContent(contentType, contentId) {
    if (!TOKEN) {
        window.location.href = 'pages/login.html';
        return;
    }
    
    const payload = {
        content_type: contentType,
    };
    payload[contentType] = contentId;
    
    fetch(`${API_BASE_URL}/likes/`, {
        method: 'POST',
        headers: {
            'Authorization': `Token ${TOKEN}`,
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(payload)
    })
    .then(response => response.json())
    .then(data => {
        console.log('Liked successfully!');
    })
    .catch(error => console.error('Error:', error));
}

// Post Comment
function postComment(contentType, contentId, text) {
    if (!TOKEN) {
        window.location.href = 'pages/login.html';
        return;
    }
    
    const payload = {
        content_type: contentType,
        text: text
    };
    payload[contentType] = contentId;
    
    fetch(`${API_BASE_URL}/comments/`, {
        method: 'POST',
        headers: {
            'Authorization': `Token ${TOKEN}`,
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(payload)
    })
    .then(response => response.json())
    .then(data => {
        console.log('Comment posted!');
        loadComments(contentType, contentId);
    })
    .catch(error => console.error('Error:', error));
}

// Load Comments
function loadComments(contentType, contentId) {
    fetch(`${API_BASE_URL}/comments/?${contentType}=${contentId}`)
    .then(response => response.json())
    .then(data => {
        const container = document.getElementById('comments-container');
        if (container && data.results) {
            container.innerHTML = data.results.map(comment => `
                <div class="comment-item">
                    <div class="comment-avatar">${comment.user.username.charAt(0).toUpperCase()}</div>
                    <div class="comment-content">
                        <div class="comment-header">
                            <span class="comment-username">${comment.user.username}</span>
                            <span class="comment-time">${formatDate(comment.created_at)}</span>
                        </div>
                        <p class="comment-text">${comment.text}</p>
                        <div class="comment-actions">
                            <a href="#" class="comment-action" onclick="likeComment(${comment.id})">
                                <i class="fas fa-thumbs-up"></i> ${comment.likes_count}
                            </a>
                            <a href="#" class="comment-action" onclick="replyComment(${comment.id})">Reply</a>
                        </div>
                    </div>
                </div>
            `).join('');
        }
    })
    .catch(error => console.error('Error loading comments:', error));
}

// Utility Functions
function likeComment(commentId) {
    console.log('Liked comment:', commentId);
}

function replyComment(commentId) {
    console.log('Reply to comment:', commentId);
}

// Format Date
function formatDate(dateString) {
    const options = { year: 'numeric', month: 'short', day: 'numeric' };
    return new Date(dateString).toLocaleDateString(undefined, options);
}

// Show Notification
function showNotification(message, type = 'info') {
    const alertDiv = document.createElement('div');
    alertDiv.className = `alert alert-${type} alert-dismissible fade show`;
    alertDiv.innerHTML = `
        ${message}
        <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
    `;
    document.body.insertBefore(alertDiv, document.body.firstChild);
}
