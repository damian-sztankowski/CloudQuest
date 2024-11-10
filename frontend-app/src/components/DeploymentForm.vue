<template>
  <div id="app">
    <!-- Logo and Title -->
    <div class="logo-container">
      <img class="logo" alt="CloudCraft Logo" src="@/assets/craft-logo2.svg" />
    </div>

    <!-- Typing Animation for Title -->
    <div class="title-container">
      <h1 class="main-title">{{ typedTitle }}</h1>
    </div>

    <!-- Description -->
    <p class="description">
      Learn real-world cloud engineering skills with hands-on challenges.
    </p>

    <!-- Divider -->
    <div class="divider"></div>

    <!-- Search Field -->
    <div class="search-container">
      <input
        v-model="searchQuery"
        class="search-input"
        type="text"
        placeholder="Search challenges..."
        @input="filterChallenges"
      />
    </div>

    <div class="main-content">
      <!-- Filter Sidebar -->
      <div class="filter-sidebar">
        <h4>Filter by Technology</h4>
        <ul>
          <li v-for="tech in technologies" :key="tech" @click="filterByTech(tech)">
            <input type="checkbox" :checked="selectedTech.includes(tech)" />
            {{ tech }}
          </li>
        </ul>
      </div>

      <!-- Challenges Grid -->
      <div class="challenges-grid">
        <div
          class="challenge"
          v-for="challenge in filteredChallenges"
          :key="challenge.id"
          @click="openPopup(challenge)"
        >
          <div class="challenge-card">
            <div class="tech-icons">
              <img v-for="(tech, index) in challenge.technologies" :key="index" :src="tech" alt="Tech Icon" class="tech-icon" />
            </div>
            <h3>{{ challenge.title }}</h3>
            <p>{{ challenge.description }}</p>
          </div>
        </div>
      </div>
    </div>

    <!-- Popup Modal -->
    <div v-if="showPopup" class="popup-overlay" @click.self="closePopup">
      <div class="popup-content">
        <!-- Close Icon -->
        <div class="close-icon" @click="closePopup">✖</div>
        
        <h3>{{ selectedChallenge.title }}</h3>
        <p>{{ selectedChallenge.description }}</p>
        <div class="popup-tech-icons">
          <img v-for="(tech, index) in selectedChallenge.technologies" :key="index" :src="tech" alt="Tech Icon" class="tech-icon" />
        </div>

        <!-- Deploy / Destroy Actions -->
        <div v-if="!showInputForm">
          <div class="popup-actions">
            <button @click="prepareForm(selectedChallenge)">Deploy</button>
            <button @click="destroyChallenge(selectedChallenge)">Destroy</button>
          </div>
        </div>

        <!-- Form for Deploy Inputs -->
        <div v-if="showInputForm">
          <h4>Enter Deployment Details for {{ requiredInput }}:</h4>
          <input type="text" v-model="deploymentInput" :placeholder="'Enter ' + requiredInput" />
          <button @click="startDeployment">Submit</button>
        </div>

        <!-- Output Window -->
        <div v-if="showOutput">
          <h4>Deployment Status:</h4>
          <div class="output-window">{{ deploymentStatus }}</div>
        </div>
      </div>
    </div>

    <!-- Professional Static Footer -->
    <footer class="footer">
      <div class="footer-content">
        <div class="footer-left">
          <p>&copy; 2024 CloudTinker by damiansztankowski</p>
          <p>License: MIT License</p>
        </div>
        <div class="footer-right">
          <p><a href="https://github.com/damiansztankowski/bau-simulator" target="_blank" rel="noopener noreferrer">GitHub Repository</a></p>
          <p><a href="https://github.com/damiansztankowski/bau-simulator/blob/deployment-logic/Contribution.md" target="_blank" rel="noopener noreferrer">Contribution Guidelines</a></p>
          <p><a href="https://github.com/your-username/your-repo#readme" target="_blank" rel="noopener noreferrer">Project Documentation (README)</a></p>
        </div>
      </div>
    </footer>
  </div>
</template>

<script>
export default {
  data() {
    return {
      searchQuery: '',
      selectedTech: [],
      technologies: ['Terraform', 'Docker', 'Google Cloud', 'Jenkins'],
      challenges: [
        {
          id: 1,
          title: 'Deploy a Web Application',
          description: 'Set up and deploy a full-stack web application on Google Cloud using Terraform.',
          technologies: [
            require('@/assets/terraform-svgrepo-com.svg'),
            require('@/assets/docker-svgrepo-com.svg'),
          ],
          requiredInput: 'projectID'
        },
        {
          id: 2,
          title: 'Create IAM Roles',
          description: 'Design and manage IAM roles with proper permissions in Google Cloud.',
          technologies: [
            require('@/assets/gcp-svgrepo-com.svg'),
            require('@/assets/terraform-svgrepo-com.svg')
          ],
          requiredInput: 'folderID'
        },
        {
          id: 3,
          title: 'Implement CI/CD Pipeline',
          description: 'Create a CI/CD pipeline for automated deployment.',
          technologies: [
            require('@/assets/git-svgrepo-com.svg'),
            require('@/assets/jenkins-svgrepo-com.svg')
          ],
          requiredInput: 'orgID'
        },
        {
          id: 4,
          title: 'Test',
          description: 'Create a CI/CD pipeline for automated deployment.',
          technologies: [
            require('@/assets/git-svgrepo-com.svg'),
            require('@/assets/jenkins-svgrepo-com.svg')
          ],
          requiredInput: 'orgID'
        }
      ],
      filteredChallenges: [],
      title: 'CloudQuest: Real-World Engineer Simulator',
      typedTitle: '',
      typingSpeed: 100,
      showPopup: false,
      selectedChallenge: null,
      showInputForm: false,
      deploymentInput: '',
      requiredInput: '',
      showOutput: false,
      deploymentStatus: 'Waiting for deployment...'
    };
  },
  created() {
    this.filteredChallenges = this.challenges;
    this.typeTitle();
  },
  methods: {
    filterChallenges() {
      this.filteredChallenges = this.challenges.filter(challenge =>
        challenge.title.toLowerCase().includes(this.searchQuery.toLowerCase())
      );
    },
    filterByTech(tech) {
      if (this.selectedTech.includes(tech)) {
        this.selectedTech = this.selectedTech.filter(item => item !== tech);
      } else {
        this.selectedTech.push(tech);
      }
      this.applyFilters();
    },
    applyFilters() {
      this.filteredChallenges = this.challenges.filter(challenge =>
        this.selectedTech.every(tech => challenge.technologies.includes(require(`@/assets/${tech}-svgrepo-com.svg`)))
      );
    },
    typeTitle() {
      let index = 0;
      const interval = setInterval(() => {
        if (index < this.title.length) {
          this.typedTitle += this.title[index];
          index++;
        } else {
          clearInterval(interval);
        }
      }, this.typingSpeed);
    },
    openPopup(challenge) {
      this.selectedChallenge = challenge;
      this.showPopup = true;
    },
    closePopup() {
      this.showPopup = false;
      this.showInputForm = false;
      this.showOutput = false;
      this.deploymentStatus = 'Waiting for deployment...';
    },
    prepareForm(challenge) {
      this.requiredInput = challenge.requiredInput;
      this.showInputForm = true;
    },
    startDeployment() {
      this.showInputForm = false;
      this.showOutput = true;
      this.deploymentStatus = `Starting deployment for ${this.deploymentInput} (${this.requiredInput})...`;

      setTimeout(() => {
        this.deploymentStatus = `Deployment successful for ${this.deploymentInput}!`;
      }, 3000);
    },
    destroyChallenge(challenge) {
      alert(`Destroying: ${challenge.title}`);
    }
  }
};
</script>

<style scoped>
/* Styles here are scoped to this component to avoid global conflicts */

/* General Styles */
body {
  margin: 0;
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  background: linear-gradient(to bottom right, #f2e3e3, #d8e3ef);
}

#app {
  color: #2c3e50;
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 20px;
  animation: fadeIn 1.5s ease-in-out;
  height: auto;
}

@keyframes fadeIn {
  from {
    opacity: 0;
  }
  to {
    opacity: 1;
  }
}

.logo-container {
  margin-top: -60px;
  animation: bounce 2s infinite;
}

.logo {
  width: 300px;
}

.title-container {
  width: 100%;
  max-width: 800px;
  margin-left: -550px;
}

.main-title {
  font-size: 3.5em;
  color: #2c3e50;
  text-align: center;
  margin: 5px 0;
  font-family: 'Courier', monospace;
  white-space: nowrap;
  overflow: hidden;
  border-right: 3px solid #2c3e50;
  width: fit-content;
  margin: 0 auto;
  animation: blinkCursor 0.8s steps(1) infinite;
}

@keyframes blinkCursor {
  0% {
    border-right-color: #2c3e50;
  }
  50% {
    border-right-color: transparent;
  }
  100% {
    border-right-color: #2c3e50;
  }
}

.description {
  font-size: 1.5em;
  color: #718096;
  margin-bottom: 20px;
  text-align: center;
}

.divider {
  width: 80%;
  border-bottom: 1px solid #e2e8f0;
  margin-bottom: 20px;
}

/* Search Field */
.search-container {
  display: flex;
  justify-content: center;
  margin: 10px 0;
}

.search-input {
  width: 100%;
  max-width: 500px;
  padding: 10px;
  font-size: 1.2em;
  border-radius: 8px;
  border: 1px solid #ccc;
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
}

.search-input:hover,
.search-input:focus {
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.2);
}

/* Main Content */
.main-content {
  display: flex;
  justify-content: center;
  align-items: flex-start;
  margin-top: 20px;
  width: 100%;
  max-width: 1200px;
  flex-grow: 1;
}

.filter-sidebar {
  width: 20%;
  background-color: #f9f9f9;
  padding: 30px;
  border-radius: 10px;
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.1);
  margin-right: 40px;
}

.filter-sidebar h4 {
  margin-bottom: 15px;
}

.filter-sidebar ul {
  list-style: none;
  padding: 0;
}

.filter-sidebar li {
  margin-bottom: 10px;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.filter-sidebar li:hover {
  background-color: #e9ecef;
}

/* Challenges Grid */
.challenges-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 20px;
  width: 75%;
  margin-bottom: 40px;
}

/* Challenge Card */
.challenge-card {
  background-color: #ffffff;
  border-radius: 12px;
  padding: 20px;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
  cursor: pointer;
  transition: transform 0.3s, box-shadow 0.3s;
  text-align: center;
  max-width: 300px;
  height: 300px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

.challenge-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 8px 16px rgba(0, 0, 0, 0.12);
}

/* Popup Styles */
.popup-overlay {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-color: rgba(0, 0, 0, 0.5);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 1000;
}

.popup-content {
  background-color: white;
  padding: 20px;
  border-radius: 10px;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.3);
  width: 400px;
  text-align: center;
  position: relative;
}

.popup-tech-icons img {
  width: 50px;
  height: auto;
  margin: 10px;
}

.popup-actions {
  margin-top: 20px;
}

.popup-actions button {
  padding: 10px 20px;
  margin-right: 10px;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

.popup-actions button:nth-child(1) {
  background-color: #4caf50;
  color: white;
}

.popup-actions button:nth-child(2) {
  background-color: #f44336;
  color: white;
}

/* Close Icon Styles */
.close-icon {
  position: absolute;
  top: 10px;
  right: 10px;
  font-size: 20px;
  cursor: pointer;
  color: #888;
  transition: color 0.2s ease;
}

.close-icon:hover {
  color: #ff0000;
}

/* Footer Styles */
.footer {
  padding: 20px;
  width: 100%;
  position: relative;
  bottom: 0;
  border-top: 1px solid #e2e8f0;
}

.footer-content {
  display: flex;
  justify-content: space-between;
  align-items: center;
  max-width: 1200px;
  margin: 0 auto;
}

.footer-left {
  font-size: 0.9em;
  color: #718096;
}

.footer-right a {
  color: #2c3e50;
  text-decoration: none;
  margin-left: 15px;
}

.footer-right a:hover {
  text-decoration: underline;
  color: #1a202c;
}

.tech-icons img {
  width: auto;
  max-width: 60px;
  max-height: 60px;
  margin: 10px;
  transition: transform 0.3s ease;
}

.tech-icons img:hover {
  transform: scale(1.1);
}
</style>
