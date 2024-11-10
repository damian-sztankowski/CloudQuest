<template>
  <div id="app">
    <!-- Animated Logo -->
    <div class="logo-container">
      <img class="logo" alt="Vue logo" src="@/assets/craft-logo2.svg">
    </div>

    <!-- Typing Animation -->
    <TypingAnimation text="CloudCraft: Real-World Engineer Simulator" class="title" />

    <!-- Description -->
    <p class="description">
      Learn real-world cloud engineering skills with hands-on challenges.
    </p>

    <!-- Challenges Grid -->
    <div class="challenges-grid">
      <div class="challenge" v-for="challenge in challenges" :key="challenge.id" @click="selectChallenge(challenge)">
        <div class="challenge-card">
          <div class="tech-icons">
            <img v-for="(tech, index) in challenge.technologies" :key="index" :src="tech" alt="Tech Icon" class="tech-icon">
          </div>
          <h3>{{ challenge.title }}</h3>
          <p>{{ challenge.description }}</p>
        </div>
      </div>
    </div>

    <!-- Subcard for selected challenge -->
    <div v-if="selectedChallenge" class="subcard">
      <h4>{{ selectedChallenge.title }}</h4>
      <p>{{ selectedChallenge.description }}</p>
      <button @click="deployChallenge(selectedChallenge)">Deploy</button>
      <button @click="destroyChallenge(selectedChallenge)">Destroy</button>
    </div>

    <!-- Footer -->
    <footer class="footer">
      <div class="footer-content">
        <p>&copy; 2024 TheCloudlyNomad.</p>
        <p>
          <a href="https://github.com/your-username/your-repo" target="_blank" rel="noopener noreferrer">GitHub Repository</a>
        </p>
        <p class="description">
          CloudCraft is an open-source project designed to help learners acquire real-world cloud engineering skills.
        </p>
        <p>License: MIT License</p>
        <p>
          Contributions are welcome! Check out our <a href="https://github.com/your-username/your-repo/blob/main/CONTRIBUTING.md" target="_blank" rel="noopener noreferrer">Contribution Guidelines</a>.
        </p>
        <p>
          For more information, visit our <a href="https://github.com/your-username/your-repo#readme" target="_blank" rel="noopener noreferrer">README</a>.
        </p>
      </div>
    </footer>
  </div>
</template>

<script>
import TypingAnimation from './TypingAnimation.vue'

export default {
  name: 'App',
  components: {
    TypingAnimation
  },
  data() {
    return {
      challenges: [
        {
          id: 1,
          title: 'Deploy a Web Application',
          description: 'Set up and deploy a full-stack web application on Google Cloud using Terraform.',
          technologies: [
            require('@/assets/terraform-svgrepo-com.svg'),
            require('@/assets/docker-svgrepo-com.svg'),
          ]
        },
        {
          id: 2,
          title: 'Create IAM Roles',
          description: 'Design and manage IAM roles with proper permissions in Google Cloud.',
          technologies: [
            require('@/assets/gcp-svgrepo-com.svg'),
            require('@/assets/terraform-svgrepo-com.svg')
          ]
        },
        {
          id: 3,
          title: 'Implement CI/CD Pipeline',
          description: 'Create a CI/CD pipeline for automated deployment.',
          technologies: [
            require('@/assets/git-svgrepo-com.svg'),
            require('@/assets/jenkins-svgrepo-com.svg')
          ]
        },
        // Add more challenges here
      ],
      selectedChallenge: null, // State to track the clicked challenge
    }
  },
  methods: {
    selectChallenge(challenge) {
      this.selectedChallenge = challenge; // Update the selected challenge
    },
    async deployChallenge(challenge) {
      // Call the backend to deploy the selected challenge
      await fetch('/api/deploy', {
        method: 'POST',
        body: JSON.stringify({ challengeId: challenge.id }),
      });
    },
    async destroyChallenge(challenge) {
      // Call the backend to destroy the selected challenge
      await fetch('/api/destroy', {
        method: 'POST',
        body: JSON.stringify({ challengeId: challenge.id }),
      });
    }
  }
}
</script>