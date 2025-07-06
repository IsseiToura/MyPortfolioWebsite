export class UIManager {
  static addChatBubble(
    text,
    sender,
    chatArea,
    linksData = null,
    isError = false
  ) {
    const bubble = document.createElement("div");
    bubble.className = `d-flex w-100 ${
      sender === "user" ? "justify-content-end" : "justify-content-start"
    }`;

    const inner = document.createElement("div");
    let bubbleClass = `chat-bubble ${
      sender === "user" ? "chat-bubble-user" : "chat-bubble-ai"
    }`;

    // if it is an error message, apply special styles
    if (isError) {
      bubbleClass += " chat-bubble-error";
    }

    inner.className = bubbleClass;
    inner.innerHTML = this.convertTextToHtml(text);

    if (sender !== "user" && linksData && linksData.length > 0) {
      const linksUl = document.createElement("ul");
      linksUl.className = "mt-2 mb-1 ps-3";

      const linksArray =
        typeof linksData === "string" ? linksData.split("\n") : linksData;

      linksArray.forEach((linkText) => {
        if (!linkText.trim()) return;
        const li = document.createElement("li");
        const a = document.createElement("a");
        const urlMatch = linkText.match(/https?:\/\/[^"\s]+/);
        const url = urlMatch ? urlMatch[0] : "#";
        a.href = url;
        a.textContent = linkText;
        a.target = "_blank";
        a.className = "link-primary";
        li.appendChild(a);
        linksUl.appendChild(li);
      });

      inner.appendChild(linksUl);
    }

    bubble.appendChild(inner);
    chatArea.appendChild(bubble);
  }

  static setButtonState(button, disabled) {
    button.disabled = disabled;
    if (disabled) {
      button.classList.add("opacity-50", "cursor-not-allowed");
    } else {
      button.classList.remove("opacity-50", "cursor-not-allowed");
    }
  }

  static clearChatArea(chatArea) {
    chatArea.innerHTML = "";
  }

  static convertTextToHtml(text) {
    let html = text.replace(/\*\*(.+?)\*\*/g, "<strong>$1</strong>");
    html = html.replace(/\n/g, "<br>");
    return html;
  }
}
