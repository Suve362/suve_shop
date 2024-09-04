document.addEventListener('DOMContentLoaded', function() {
    const inputs = document.querySelectorAll('.field__input');

    inputs.forEach(input => {
        const label = input.previousElementSibling;
        if (input.value) {
            label.style.top = '-10px';
            label.style.fontSize = '12px';
            label.style.color = '#362';
        }

        input.addEventListener('focus', () => {
            label.style.top = '-10px';
            label.style.fontSize = '12px';
            label.style.color = '#362';
        });

        input.addEventListener('blur', () => {
            if (!input.value) {
                label.style.top = '50%';
                label.style.fontSize = '16px';
                label.style.color = '#777780';
            }
        });
    });
});
