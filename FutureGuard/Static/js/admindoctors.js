
    function populateEditModal(doctorId, doctorName, specialization, contact) {
    document.getElementById('editDoctorName').value = doctorName;
    document.getElementById('editSpecialization').value = specialization;
    document.getElementById('editContact').value = contact;

    // Update the form action to include the doctor ID
    var form = document.getElementById('editDoctorForm');
    form.action = "{% url 'edit_doctor' 0 %}".replace(/0$/, doctorId);
  }