async function login(username, password) {
    return fetch('http://localhost:8000/api/user/login/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            username: username,
            password: password
        })
    }).then(response => {
        if (response.ok) {
            return response.json();
        } else {
            throw new Error('Error during login');
        }
    })
}

async function register(username, password) {
    return fetch('http://localhost:8000/api/user/register', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            username: username,
            password: password
        })
    }).then(response => {
        if (response.ok) {
            return response.json();
        } else {
            throw new Error('Error during register');
        }
    })
}

function logout() {
    localStorage.removeItem('token');
}

async function getUser(username) {
    return fetch('http://localhost:8000/api/user/' + username, {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': 'Token ' + JSON.parse(localStorage.getItem('token'))
        }
    }).then(response => {
        if (response.ok) {
            return response.json();
        } else {
            throw new Error('Error during get user');
        }
    })
}

export {
    login,
    register,
    logout,
    getUser
}
