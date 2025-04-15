"use client";

import React from "react";

type Message = {
  role: "user" | "bot";
  text: string;
};

interface Props {
  messages: Message[];
}

const ChatDisplay: React.FC<Props> = ({ messages }) => {
  return (
    <div className="flex flex-col gap-3 p-4">
      {messages.map((msg, idx) => (
        <div
          key={idx}
          className={`flex w-full animate-fade-in ${
            msg.role === "user" ? "justify-end" : "justify-start"
          }`}
        >
          <div className="relative max-w-[75%] sm:max-w-[60%] md:max-w-[50%]">
            {/* Chat bubble */}
            <div
              className={`p-3 rounded-2xl text-sm whitespace-pre-wrap break-words shadow-md ${
                msg.role === "user"
                  ? "bg-blue-500 text-white text-right rounded-br-none"
                  : "bg-neutral-800 text-white text-left rounded-bl-none"
              }`}
            >
              {msg.text}
            </div>

            {/* Bubble tail */}
            {msg.role === "user" ? (
              <div className="absolute bottom-0 right-[-10px] w-0 h-0 border-t-[10px] border-t-blue-500 border-l-[10px] border-l-transparent" />
            ) : (
              <div className="absolute bottom-0 left-[-10px] w-0 h-0 border-t-[10px] border-t-neutral-800 border-r-[10px] border-r-transparent" />
            )}
          </div>
        </div>
      ))}
    </div>
  );
};

export default ChatDisplay;
