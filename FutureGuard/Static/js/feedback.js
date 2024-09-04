document.addEventListener('DOMContentLoaded', function () {
    const stars = document.querySelectorAll('.rating label');
    let selectedValue = 0;

    stars.forEach((star, index) => {
        // Click event to set the selected value
        star.addEventListener('click', function () {
            selectedValue = index + 1;
            updateStars(selectedValue);
        });

        // Mouseover event to highlight stars on hover
        star.addEventListener('mouseover', function () {
            updateStars(index + 1);
        });

        // Mouseout event to revert to the selected value when not hovering
        star.addEventListener('mouseout', function () {
            updateStars(selectedValue);
        });
    });

    // Function to update the stars based on the value
    function updateStars(value) {
        stars.forEach((star, index) => {
            if (index < value) {
                star.classList.add('selected');
            } else {
                star.classList.remove('selected');
            }
        });
    }
});




// document.addEventListener('DOMContentLoaded', function () {
//     const stars = document.querySelectorAll('.rating label');
//     let selectedValue = 0;

//     stars.forEach((star, index) => {
//         star.addEventListener('click', function () {
//             selectedValue = index + 1;
//             updateStars();
//         });

//         star.addEventListener('mouseover', function () {
//             updateStars(index + 1);
//         });

//         star.addEventListener('mouseout', function () {
//             updateStars(selectedValue);
//         });
//     });

//     function updateStars(value) {
//         stars.forEach((star, index) => {
//             if (index < value) {
//                 star.classList.add('selected');
//             } else {
//                 star.classList.remove('selected');
//             }
//         });
//     }
// });
