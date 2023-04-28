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

async function shareProject(id) {
  return fetch(`${API_URL}/project/share/${id}/`, {
    method: "POST",
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
  return fetch(`${API_URL}/project/public/${id}/`, {
    method: "POST",
    body: {
      public: makePublic,
    },
    headers: getHeaders(),
  }).then((response) => {
    if (response.ok) {
      return response.json();
    } else {
      throw new Error("Error during make public project");
    }
  });
}

async function createFile(id) {
  return fetch(`${API_URL}/project/${id}/create_file/`, {
    method: "POST",
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

export {
  getProject,
  createProject,
  shareProject,
  changeProjectVisibility,
  createFile,
  deleteProject,
  searchProjects,
};
