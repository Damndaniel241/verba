import { defineStore } from "pinia";
import { ref } from "vue";
import { useAuthStore } from "./auth";

const auth = useAuthStore();


export const useChatStore = defineStore("chat", () => {
  const socket = ref<WebSocket | null>(null);
  const messages = ref<any[]>([]);



  function connect(roomId: string, accessToken: string) {
    socket.value = new WebSocket(
      `ws://127.0.0.1:8000/ws/chat/${roomId}/?token=${accessToken}`
    );

    socket.value.onopen = () => {
      console.log("[WS] Connected");
    };

    socket.value.onmessage = (event: MessageEvent) => {
      const data = JSON.parse(event.data);
      messages.value.push(data);
      console.log("[WS] Message:", data);
    };

    socket.value.onclose = () => {
      console.log("[WS] Closed");
    };

    socket.value.onerror = (e) => {
      console.error("[WS] Error", e);
    };

  
  }


  function sendMessage(content: string) {
    if (socket.value && socket.value.readyState === WebSocket.OPEN) {
      socket.value.send(JSON.stringify({
        type: "chat_message",
        message: content,
        sender: auth.userId,
      }));


      // console.log("i sent a message nigga");
      
    }
  }

  function disconnect() {
    if (socket.value) {
      socket.value.close();
      socket.value = null;
      messages.value = [];
    }
     console.log("i disconnected nigga");
  }

  return { socket, messages, sendMessage, connect, disconnect }

},{
  persist: true   // ✅ this tells Pinia to persist the store
})