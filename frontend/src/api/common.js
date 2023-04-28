const API_URL = "http://localhost:8000/api";

function getHeaders(auth = true) {
  return auth
    ? {
        "Content-Type": "application/json",
        Authorization: `Token ${localStorage.getItem("token")}`,
      }
    : {
        "Content-Type": "application/json",
      };
}

export { API_URL, getHeaders };
