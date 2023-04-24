async function login(username, password) {
  return fetch("http://localhost:8000/api/user/login/", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      username: username,
      password: password,
    }),
  }).then((response) => {
    if (response.ok) {
      return response.json();
    } else {
      throw new Error("Error during login");
    }
  });
}

async function register(username, email, firstName, lastName, password) {
  return fetch("http://localhost:8000/api/user/register/", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
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
    } else {
      throw new Error("Error during register");
    }
  });
}

async function getUser(username) {
  return fetch(`http://localhost:8000/api/user/${username}/`, {
    method: "GET",
    headers: {
      "Content-Type": "application/json",
      Authorization: "Token " + localStorage.getItem("token"),
    },
  }).then((response) => {
    console.log(response);
    if (response.ok) {
      return response.json();
    } else {
      throw new Error("Error during get user");
    }
  });
}

export { login, register, getUser };
