/**
 * chat-manager.js - Manages chat state and scroll behavior
 */

export class ChatManager {
  constructor() {
    this.lastQuestion = "";
    this.lastAnswer = "";
    this.chatArea = document.getElementById("chatArea");
  }

  updateLastQuestion(question) {
    this.lastQuestion = question;
  }

  updateLastAnswer(answer) {
    this.lastAnswer = answer;
  }

  scrollToBottom() {
    this.chatArea.scrollTop = this.chatArea.scrollHeight;
  }
}
