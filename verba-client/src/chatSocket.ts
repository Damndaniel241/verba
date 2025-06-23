export function createChatSocket(roomId:string, accessToken: string): WebSocket{
    const socket = new WebSocket(
        `ws://127.0.0.1:8000/ws/chat/${roomId}/token=${accessToken}`
    );


    socket.onopen = () =>{
        console.log("[WS connected to room:", roomId);
    };


    socket.onmessage = (event:MessageEvent) =>{
        const data = JSON.parse(event.data);
        console.log("[WS] Message received: ", data);
        // Dispatch to store or UI as needed
    };

    socket.onerror = (error:Event) => {
        console.error("[WS] Error:", error);
       
    };


    socket.onclose = (event:CloseEvent)=>{
        console.warn("[WS] Disconnected: ", event.reason || "No reason")
         // Optional: auto-reconnect logic here
    };


    return {socket,createChat};
}

