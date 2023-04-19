async function getFile(id) {
    fetch('http://localhost:8000/api/file/' + id, {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': 'Token ' + JSON.parse(localStorage.getItem('token'))
        }
    }).then(response => {
        if (response.ok) {
            return response.json();
        } else {
            throw new Error('Error during get file');
        }
    })
}

async function syncFile(id, newContent) {
    return fetch('http://localhost:8000/api/file/sync/' + id, {
        method: 'PATCH',
        body: {
            content: newContent
        },
        headers: {
            'Content-Type': 'application/json',
            'Authorization': 'Token ' + JSON.parse(localStorage.getItem('token'))
        }
    }).then(response => {
        if (response.ok) {
            return response.json();
        } else {
            throw new Error('Error during sync file');
        }
    })
}

async function deleteFile(id) {
    return fetch('http://localhost:8000/api/file/' + id + '/delete', {
        method: 'DELETE',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': 'Token ' + JSON.parse(localStorage.getItem('token'))
        }
    }).then(response => {
        if (response.ok) {
            return response.json();
        } else {
            throw new Error('Error during delete file');
        }
    })
}

export {
    getFile,
    syncFile,
    deleteFile
}
