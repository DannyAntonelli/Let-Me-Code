<template>
  <font-awesome-icon
    icon="fa-solid fa-pen-to-square"
    size="xs"
    class="ms-3"
    @click="editProfile"
    style="cursor: pointer"
    data-bs-toggle="modal"
    data-bs-target="#editProfile"
  />

  <div
    class="modal fade"
    id="editProfile"
    tabindex="-1"
    aria-labelledby="editProfileLabel"
    aria-hidden="true"
  >
    <div class="modal-dialog modal-dialog-centered">
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title" id="editProfileLabel">Edit Profile</h5>
          <button
            type="button"
            class="btn-close btn-xs"
            data-bs-dismiss="modal"
            aria-label="Close"
          ></button>
        </div>

        <div class="modal-body">
          <form>
            <label for="edit-profile-first-name" class="col-form-label"
              >First Name:</label
            >
            <input
              type="text"
              class="form-control"
              id="edit-profile-first-name"
              placeholder="First Name"
              v-model="newFirstName"
            />

            <label for="edit-profile-last-name" class="col-form-label"
              >Last Name:</label
            >
            <input
              type="text"
              class="form-control"
              id="edit-profile-last-name"
              placeholder="Last Name"
              v-model="newLastName"
            />

            <label for="edit-profile-email" class="col-form-label"
              >Email:</label
            >
            <input
              type="text"
              class="form-control"
              id="edit-profile-email"
              placeholder="Email"
              v-model="newEmail"
            />
          </form>
        </div>

        <div class="modal-footer">
          <button
            type="button"
            class="btn btn-secondary"
            data-bs-dismiss="modal"
            id="dismiss-edit-profile-modal"
          >
            Cancel
          </button>
          <button
            type="button"
            class="btn btn-success"
            data-dismiss="modal"
            @click="editProfile"
            style="
              background-color: var(--bs-purple);
              border-color: var(--bs-purple);
            "
          >
            Save Profile
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "EditProfileButton",

  props: {
    firstName: {
      type: String,
      required: true,
    },
    lastName: {
      type: String,
      required: true,
    },
    email: {
      type: String,
      required: true,
    },
  },

  data() {
    return {
      newFirstName: this.firstName,
      newLastName: this.lastName,
      newEmail: this.email,
    };
  },

  methods: {
    editProfile() {
      this.$emit("edit-profile", {
        firstName: this.newFirstName,
        lastName: this.newLastName,
        email: this.newEmail,
      });
      document.getElementById("dismiss-edit-profile-modal").click();
    },
  },
};
</script>

<style scoped>
button {
  font-size: 1rem;
}
label {
  font-size: 1rem;
}
</style>
