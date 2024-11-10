<template>
  <div id="app">

    <!-- Your existing components -->
    <DeploymentForm msg="Welcome to Your Vue.js App" />
  </div>
</template>

<script>
import DeploymentForm from './components/DeploymentForm.vue';


export default {
  name: 'App',
  components: {
    DeploymentForm
  },
};
</script>

