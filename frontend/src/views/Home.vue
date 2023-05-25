<template>
  <h1 class="text-center p-5 mt-5">
    <font-awesome-icon icon="fa-solid fa-terminal" beat-fade />
    <strong> Code, Share, Collaborate</strong>
  </h1>

  <div class="container text-center text-md-start">
    <div class="row mt-5 text-center">
      <div class="col-12 col-sm-6 col-md-6 mx-auto mb-4">
        <p>
          <strong> Let Me Code</strong> is a platform for developers to share
          their code, collaborate with other developers, and learn from each
          other. Create public and private projects and share them with other
          people.
        </p>
      </div>

      <div class="col-12 col-sm-6 col-md-4 mx-auto mb-4">
        <h5><strong>Join Our Community:</strong></h5>
        <router-link to="/register"
          ><button
            class="btn btn-primary btn-lg"
            style="
              background-color: var(--bs-purple);
              border-color: var(--bs-purple);
            "
          >
            Start for free
          </button></router-link
        >
      </div>
    </div>
  </div>

  <div class="container text-center text-md-start mt-5 pt-2">
    <div class="row mt-3 text-center">
      <div class="col-12 col-sm-6 col-md-4 mx-auto mb-4 hidden">
        <h4><strong>Zero Setup</strong></h4>
        <p>
          Start working on your code instantly, without having any code editor
          or IDE installed on your machine. Work effortlessly on your PC,
          smartphone or smartfridge (ok maybe that's not recommended).
        </p>
      </div>

      <div class="col-12 col-sm-6 col-md-4 mx-auto mb-4 hidden" id="two">
        <h4><strong>Collaborate Flawlessly with your Colleagues</strong></h4>
        <p>
          Create your new project, share it with your friend and start working
          together. Keep your changes up to date in real time.
        </p>
      </div>

      <div class="col-12 col-sm-6 col-md-4 mx-auto mb-4 hidden" id="three">
        <h4><strong>Join +10M Developers</strong></h4>
        <p>
          Our community currently counts more than 10 million developers and
          over 40 million projects. Let yourself be inspired!
        </p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "Home",

  async mounted() {
    const observer = new IntersectionObserver((entries) => {
      entries.forEach((entry) => {
        console.log(entry);
        if (entry.isIntersecting > 0) {
          entry.target.classList.add("show");
        } else {
          entry.target.classList.remove("show");
        }
      });
    });

    document
      .querySelectorAll(".hidden")
      .forEach((element) => observer.observe(element));
  },
};
</script>

<style scoped>
a {
  color: inherit;
}

#two {
  transition-delay: 200ms;
}

#three {
  transition-delay: 400ms;
}
</style>
