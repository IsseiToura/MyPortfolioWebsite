export class ApiService {
  static async askQuestion(question) {
    const response = await fetch("/api/issei_gpt/ask", {
      method: "POST",
      body: new URLSearchParams({ question: question }),
      headers: { "Content-Type": "application/x-www-form-urlencoded" },
    });

    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }

    return await response.json();
  }
}
