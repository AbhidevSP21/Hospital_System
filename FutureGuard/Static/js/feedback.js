document.addEventListener('DOMContentLoaded', function () {
    const stars = document.querySelectorAll('.rating label');
    let selectedValue = 0;

    stars.forEach((star, index) => {
        star.addEventListener('click', function () {
            selectedValue = index + 1;
            updateStars();
        });

        star.addEventListener('mouseover', function () {
            updateStars(index + 1);
        });

        star.addEventListener('mouseout', function () {
            updateStars(selectedValue);
        });
    });

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
