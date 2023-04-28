import { API_URL, getHeaders } from "./common";

async function login(username, password) {
  return fetch(`${API_URL}/user/login/`, {
    method: "POST",
    headers: getHeaders(false),
    body: JSON.stringify({
      username: username,
      password: password,
    }),
  }).then((response) => {
    if (response.ok) {
      return response.json();
    } else if (response.status === 400) {
      throw new Error("Invalid username or password");
    } else {
      throw new Error("Error during login");
    }
  });
}

async function register(username, email, firstName, lastName, password) {
  return fetch(`${API_URL}/user/register/`, {
    method: "POST",
    headers: getHeaders(false),
    body: JSON.stringify({
      username: username,
      email: email,
      first_name: firstName,
      last_name: lastName,
      password: password,
    }),
  }).then((response) => {
    if (response.ok) {
      return response.json();
    } else if (response.status === 409) {
      throw new Error("Username already taken");
    } else {
      throw new Error("Error during register");
    }
  });
}

async function getUser(username) {
  return fetch(`${API_URL}/user/${username}/`, {
    method: "GET",
    headers: getHeaders(),
  }).then((response) => {
    console.log(response);
    if (response.ok) {
      return response.json();
    } else {
      throw new Error("Error during get user");
    }
  });
}

async function searchUsers(query) {
  return fetch(`${API_URL}/user/search/?query=${query}`, {
    method: "GET",
    headers: getHeaders(),
  }).then((response) => {
    if (response.ok) {
      return response.json();
    } else {
      throw new Error("Error during search user");
    }
  });
}

export { login, register, getUser, searchUsers };
