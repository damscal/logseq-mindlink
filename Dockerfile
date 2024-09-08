# Use the official Node.js image
FROM node:18-alpine

# Set the working directory inside the container
WORKDIR /app

# Copy package.json and package-lock.json before other files
COPY package*.json ./

# Install project dependencies
RUN npm install

# Install TypeScript globally
RUN npm install -g typescript

# Copy the rest of the application code
COPY . .

# Build the TypeScript code
RUN npm run build

# Set the command to run TypeScript compiler in watch mode
CMD ["npm", "run", "watch"]
