<Widget
    handleNewUserMessage={handleNewUserMessage}
    customComponents = {{
        datePicker: ({  sendMessage }) => (
            <input
             type="date"
             onChange={(e) => {
                const date = new Date(e.target.value);
                const formatted = date.toISOString().split("T")[0];
                sendMessage(formatted);
             }}
             />
        )
    }}
    />