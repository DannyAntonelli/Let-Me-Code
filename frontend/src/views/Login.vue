<template>
<form @submit.prevent="handleLogin">
    <div class="form-outline mb-4">
        <input type="text" id="login-username" class="form-control" v-model="username" required />
        <label class="form-label" for="login-username">Username</label>
    </div>

    <div class="form-outline mb-4">
        <input type="password" id="login-password" class="form-control" v-model="password" required />
        <label class="form-label" for="login-password">Password</label>
    </div>

    <button type="submit" class="btn btn-primary btn-block mb-4">Sign in</button>

    <div class="text-center">
        <p>Not a member? <router-link to="/register">Register</router-link>
        </p>
    </div>
</form>
</template>

<script>
import {
    login
} from '@/api/user.js'

export default {
    name: 'Login',

    data() {
        return {
            username: '',
            password: ''
        }
    },

    methods: {
        handleLogin() {
            login(this.username, this.password)
                .then(response => {
                    console.log(response)
                    localStorage.setItem('username', this.username)
                    localStorage.setItem('token', response.token)
                    this.$router.push('/')
                })
                .catch(error => {
                    console.log(error)
                })
        }
    }
}
</script>
