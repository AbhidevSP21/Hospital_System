function confirmDelete(appointmentId) {
    if (confirm("Are you sure you want to cancel this appointment?")) {
        // Add code to handle cancellation
        alert("Appointment with ID " + appointmentId + " canceled.");
    }
}
