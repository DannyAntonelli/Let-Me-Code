<template>
  <h1>{{ username }}</h1>
  <p>email: {{ email }}</p>
  <p>first name: {{ firstName }}</p>
  <p>last name: {{ lastName }}</p>
  <p>date joined: {{ dateJoined }}</p>
  <ul>
    project ids:
    <li v-for="projectId in projectIds" :key="projectId">
      {{ projectId }}
    </li>
  </ul>
  <ul>
    shared project ids:
    <li v-for="sharedProjectId in sharedProjectIds" :key="sharedProjectId">
      {{ sharedProjectId }}
    </li>
  </ul>
  <p v-if="isCurrentUser">this is your profile</p>
  <p v-else>this is not your profile</p>
</template>

<script>
  import { getUser } from "@/api/user.js";

  export default {
    name: "Profile",
    data() {
      return {
        username: "",
        email: "",
        firstName: "",
        lastName: "",
        dateJoined: "",
        projectIds: [],
        sharedProjectIds: [],
        isCurrentUser: false,
      };
    },

    async created() {
      getUser(this.$route.params.username)
        .then((response) => {
          console.log(response);
          this.username = response.user.username;
          this.email = response.user.email;
          this.firstName = response.user.first_name;
          this.lastName = response.user.last_name;
          this.dateJoined = response.user.date_joined;
          this.projectIds = response.user.project_ids;
          this.projectIds = response.projectIds;
          this.sharedProjectIds = response.sharedProjectIds;
          this.isCurrentUser =
            this.username == localStorage.getItem("username");
        })
        .catch((error) => {
          console.log(error);
        });
    },
  };
</script>
