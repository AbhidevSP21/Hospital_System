function confirmDelete(patientId) {
    if (confirm("Are you sure you want to remove this patient?")) {
        // Add code to handle deletion
        alert("Patient with ID " + patientId + " removed.");
    }
}
