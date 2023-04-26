import { API_URL, getHeaders } from "./common";

async function getFile(id) {
  return fetch(`${API_URL}/file/${id}/`, {
    method: "GET",
    headers: getHeaders(),
  }).then((response) => {
    if (response.ok) {
      return response.json();
    } else {
      throw new Error("Error during get file");
    }
  });
}

async function syncFile(id, newContent) {
  return fetch(`${API_URL}/file/sync/${id}/`, {
    method: "PATCH",
    body: {
      content: newContent,
    },
    headers: getHeaders(),
  }).then((response) => {
    if (response.ok) {
      return response.json();
    } else {
      throw new Error("Error during sync file");
    }
  });
}

async function deleteFile(id) {
  return fetch(`${API_URL}/file/${id}/delete/`, {
    method: "DELETE",
    headers: getHeaders(),
  }).then((response) => {
    if (response.ok) {
      return response.json();
    } else {
      throw new Error("Error during delete file");
    }
  });
}

export { getFile, syncFile, deleteFile };
