# Use the official Node.js image as the base
FROM node:bookworm AS build

# Set the working directory in the container
WORKDIR /app

# Copy package.json and package-lock.json to install dependencies
COPY package*.json ./

# Install application dependencies
RUN npm install

# Copy the rest of the application code
COPY . .

# Install bash
RUN apt-get update && apt-get install -y bash

# Build the application (optional, only if you have a build step)
RUN npm run build || true  # Allow build step to fail if not defined

# Start a new stage for the final image
FROM node:bookworm

# Set the working directory in the final image
WORKDIR /app

# Copy the built application from the previous stage
COPY --from=build /app /app

# Expose the port the app runs on
EXPOSE 3000 

# Command to run the application
CMD ["npm", "start"]
