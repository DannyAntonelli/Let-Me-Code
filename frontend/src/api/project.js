import { API_URL, getHeaders } from "./common";

async function getProject(id) {
  return fetch(`${API_URL}/project/${id}/`, {
    method: "GET",
    headers: getHeaders(),
  }).then((response) => {
    if (response.ok) {
      return response.json();
    } else {
      throw new Error("Error during get project");
    }
  });
}

async function createProject(name, description, isPublic) {
  return fetch(`${API_URL}/project/create_project/`, {
    method: "POST",
    headers: getHeaders(),
    body: JSON.stringify({
      name: name,
      description: description,
      is_public: isPublic.toString(),
    }),
  }).then((response) => {
    if (response.ok) {
      return response.json();
    } else {
      throw new Error("Error during create project");
    }
  });
}

async function shareProject(id, username) {
  return fetch(`${API_URL}/project/${id}/share/`, {
    method: "POST",
    body: JSON.stringify({
      username: username,
    }),
    headers: getHeaders(),
  }).then((response) => {
    if (response.ok) {
      return response.json();
    } else {
      throw new Error("Error during share project");
    }
  });
}

async function changeProjectVisibility(id, makePublic) {
  return fetch(`${API_URL}/project/${id}/public/`, {
    method: "POST",
    body: JSON.stringify({
      public: makePublic,
    }),
    headers: getHeaders(),
  }).then((response) => {
    if (response.ok) {
      return response.json();
    } else {
      throw new Error("Error during make public project");
    }
  });
}

async function createFile(id, name, language) {
  return fetch(`${API_URL}/project/${id}/create_file/`, {
    method: "POST",
    body: JSON.stringify({
      name: name,
      language: language,
    }),
    headers: getHeaders(),
  }).then((response) => {
    if (response.ok) {
      return response.json();
    } else {
      throw new Error("Error during create file");
    }
  });
}

async function deleteProject(id) {
  return fetch(`${API_URL}/project/${id}/delete/`, {
    method: "DELETE",
    headers: getHeaders(),
  }).then((response) => {
    if (response.ok) {
      return response.json();
    } else {
      throw new Error("Error during delete project");
    }
  });
}

async function searchProjects(query) {
  return fetch(`${API_URL}/project/search/?query=${query}`, {
    method: "GET",
    headers: getHeaders(),
  }).then((response) => {
    if (response.ok) {
      return response.json();
    } else {
      throw new Error("Error during search projects");
    }
  });
}

async function changeFavorite(id, makeFavorite) {
  return fetch(`${API_URL}/project/${id}/favorite/`, {
    method: "POST",
    body: JSON.stringify({
      favorite: makeFavorite,
    }),
    headers: getHeaders(),
  }).then((response) => {
    if (response.ok) {
      return response.json();
    } else {
      throw new Error("Error during change favorite");
    }
  });
}

async function getFollowingProjects() {
  return fetch(`${API_URL}/project/following/`, {
    method: "GET",
    headers: getHeaders(),
  }).then((response) => {
    if (response.ok) {
      return response.json();
    } else {
      throw new Error("Error getting following projects");
    }
  });
}

async function getFavoriteProjects() {
  return fetch(`${API_URL}/project/favorites/`, {
    method: "GET",
    headers: getHeaders(),
  }).then((response) => {
    if (response.ok) {
      return response.json();
    } else {
      throw new Error("Error getting favorite projects");
    }
  });
}

export {
  getProject,
  createProject,
  shareProject,
  changeProjectVisibility,
  createFile,
  deleteProject,
  searchProjects,
  changeFavorite,
  getFollowingProjects,
  getFavoriteProjects,
};
