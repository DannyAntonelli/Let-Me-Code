async function getProject(id) {
    return fetch(`http://localhost:8000/api/project/${id}`, {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': 'Token ' + JSON.parse(localStorage.getItem('token'))
        }
    }).then(response => {
        if (response.ok) {
            return response.json();
        } else {
            throw new Error('Error during get project');
        }
    })
}

async function createProject() {
    return fetch('http://localhost:8000/api/project/create_project/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': 'Token ' + JSON.parse(localStorage.getItem('token'))
        }
    }).then(response => {
        if (response.ok) {
            return response.json();
        } else {
            throw new Error('Error during create project');
        }
    })
}

async function shareProject(id) {
    return fetch(`http://localhost:8000/api/project/share/${id}/`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': 'Token ' + JSON.parse(localStorage.getItem('token'))
        }
    }).then(response => {
        if (response.ok) {
            return response.json();
        } else {
            throw new Error('Error during share project');
        }
    })
}

async function changeProjectVisibility(id, makePublic) {
    return fetch(`http://localhost:8000/api/project/public/${id}/`, {
        method: 'POST',
        body: {
            public: makePublic
        },
        headers: {
            'Content-Type': 'application/json',
            'Authorization': 'Token ' + JSON.parse(localStorage.getItem('token'))
        }
    }).then(response => {
        if (response.ok) {
            return response.json();
        } else {
            throw new Error('Error during make public project');
        }
    })
}

async function createFile(id) {
    return fetch(`http://localhost:8000/api/project/${id}/create_file/`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': 'Token ' + JSON.parse(localStorage.getItem('token'))
        }
    }).then(response => {
        if (response.ok) {
            return response.json();
        } else {
            throw new Error('Error during create file');
        }
    })
}

async function deleteProject(id) {
    return fetch(`http://localhost:8000/api/project/${id}/delete/`, {
        method: 'DELETE',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': 'Token ' + JSON.parse(localStorage.getItem('token'))
        }
    }).then(response => {
        if (response.ok) {
            return response.json();
        } else {
            throw new Error('Error during delete project');
        }
    })
}

export {
    getProject,
    createProject,
    shareProject,
    changeProjectVisibility,
    createFile,
    deleteProject
}
