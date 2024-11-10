<template>
    <div>
      <h1>{{ typedText }}</h1>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        text: "CloudCraft: Real-World Engineer Simulator",
        typedText: "",
        currentIndex: 0,
        typingSpeed: 100, // Speed in milliseconds
        pauseDuration: 20000, // Pause duration in milliseconds
      };
    },
    mounted() {
      this.startTypingAnimation();
    },
    methods: {
      startTypingAnimation() {
        this.typedText = ""; // Reset the typedText
        this.currentIndex = 0; // Reset the current index
        this.type(); // Start the typing
      },
      type() {
        if (this.currentIndex < this.text.length) {
          this.typedText += this.text.charAt(this.currentIndex);
          this.currentIndex++;
          // Continue typing after a delay
          setTimeout(this.type, this.typingSpeed);
        } else {
          // Wait for a while after finishing the typing
          setTimeout(() => {
            // Pause before starting to type again
            this.startTypingAnimation();
          }, this.pauseDuration);
        }
      },
    },
  };
  </script>
  
  <style scoped>
  h1 {
    font-size: 2em; /* Adjust size as needed */
    text-align: center; /* Center the text */
  }
  </style>
  