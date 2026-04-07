import { useState } from "react";
import axios from "axios";

export default function App() {
  const [message, setMessage] = useState("");
  const [chat, setChat] = useState([]);
  const [loading, setLoading] = useState(false);

  const sendMessage = async () => {
    if (!message) return;

    const newChat = [...chat, { role: "user", text: message }];
    setChat(newChat);
    setLoading(true);

    try {
      const res = await axios.post("https://8080-cs-295982677758-default.cs-asia-southeast1-seal.cloudshell.dev/chat", {
        message,
      });

      setChat([
        ...newChat,
        {
          role: "ai",
          text: JSON.stringify(res.data.response, null, 2),
        },
      ]);
    } catch (err) {
      setChat([
        ...newChat,
        { role: "ai", text: "⚠️ Error connecting to backend" },
      ]);
    }

    setMessage("");
    setLoading(false);
  };

  return (
    <div className="h-screen bg-gradient-to-br from-purple-900 via-black to-blue-900 flex flex-col items-center p-4">

      {/* Header */}
      <div className="text-white text-3xl font-bold mb-4">
        🤖 StudyOps AI
      </div>

      {/* Chat Box */}
      <div className="w-full max-w-3xl flex-1 bg-white/10 backdrop-blur-lg rounded-2xl shadow-xl p-4 overflow-y-auto">

        {chat.length === 0 && (
          <div className="text-center text-gray-300 mt-20">
            Start chatting with your AI assistant 🚀
          </div>
        )}

        {chat.map((msg, i) => (
          <div
            key={i}
            className={`mb-4 flex ${
              msg.role === "user" ? "justify-end" : "justify-start"
            }`}
          >
            <div
              className={`max-w-xs md:max-w-md p-3 rounded-xl ${
                msg.role === "user"
                  ? "bg-blue-600 text-white"
                  : "bg-gray-800 text-gray-200"
              }`}
            >
              <pre className="whitespace-pre-wrap">{msg.text}</pre>
            </div>
          </div>
        ))}

        {loading && (
          <div className="text-gray-400 animate-pulse">
            🤖 AI is thinking...
          </div>
        )}
      </div>

      {/* Input */}
      <div className="w-full max-w-3xl flex mt-4">
        <input
          className="flex-1 p-3 rounded-l-xl bg-white/10 text-white outline-none"
          placeholder="Ask anything..."
          value={message}
          onChange={(e) => setMessage(e.target.value)}
        />

        <button
          onClick={sendMessage}
          className="bg-blue-600 px-6 rounded-r-xl hover:bg-blue-700 transition"
        >
          Send
        </button>
      </div>
    </div>
  );
}