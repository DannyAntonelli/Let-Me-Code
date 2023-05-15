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

async function followUser(username, follow) {
  return fetch(`${API_URL}/user/${username}/follow/`, {
    method: "POST",
    headers: getHeaders(),
    body: JSON.stringify({
      follow: follow,
    }),
  }).then((response) => {
    if (response.ok) {
      return response.json();
    } else {
      throw new Error("Error during follow user");
    }
  });
}

async function editProfile(firstName, lastName, email) {
  return fetch(`${API_URL}/user/edit/`, {
    method: "PATCH",
    headers: getHeaders(),
    body: JSON.stringify({
      first_name: firstName,
      last_name: lastName,
      email: email,
    }),
  }).then((response) => {
    if (response.ok) {
      return response.json();
    } else {
      throw new Error("Error during edit user");
    }
  });
}

async function getFollowingUsers() {
  return fetch(`${API_URL}/user/following/`, {
    method: "GET",
    headers: getHeaders(),
  }).then((response) => {
    if (response.ok) {
      return response.json();
    } else {
      throw new Error("Error during get following user");
    }
  });
}

export {
  login,
  register,
  getUser,
  searchUsers,
  followUser,
  editProfile,
  getFollowingUsers,
};
