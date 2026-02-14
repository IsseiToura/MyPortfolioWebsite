/**
 * main.js - IsseiGPT entry point
 * Handles the main chat interface logic and coordinates between UI, API, and state management
 */

import { ChatManager } from "./chat-manager.js";
import { UIManager } from "./ui-manager.js";
import { ApiService } from "./api-service.js";

const chatManager = new ChatManager();

document
  .getElementById("questionForm")
  .addEventListener("submit", async function (event) {
    event.preventDefault();

    const question = document.getElementById("question").value;
    if (!question.trim()) return;

    const submitButton = this.querySelector("button[type='submit']");

    try {
      // UI update
      UIManager.addChatBubble(question, "user", chatManager.chatArea);
      chatManager.updateLastQuestion(question);

      // disable button
      UIManager.setButtonState(submitButton, true);

      // API call
      const data = await ApiService.askQuestion(question);
      console.log(data);

      // answer display
      UIManager.addChatBubble(
        data.answer || "No answer found.",
        "bot",
        chatManager.chatArea,
        data.links
      );
      chatManager.updateLastAnswer(data.answer || "");

      // scroll
      chatManager.scrollToBottom();
    } catch (error) {
      const errorMessage = error.message || "Something went wrong.";
      UIManager.addChatBubble(
        errorMessage,
        "bot",
        chatManager.chatArea,
        null,
        true
      );
      console.error("Error:", error);
    } finally {
      // enable button and reset form
      UIManager.setButtonState(submitButton, false);
      document.getElementById("question").value = "";
      document.getElementById("question").focus();
    }
  });

// clear chat area
const clearButton = document.getElementById("clearChat");
if (clearButton) {
  clearButton.addEventListener("click", function () {
    UIManager.clearChatArea(chatManager.chatArea);
  });
}
