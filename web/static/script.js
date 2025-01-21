function validateIpAddress(ip) {
    const IpRegex = /^(\d{1,3}\.){3}\d{1,3}$/;

    if (!IpRegex.test(ip)) {
        return false;
    }

    const octets = ip.split('.');
    return octets.every(octet => {
        const num = parseInt(octet, 10);
        return num >= 0 && num <= 255;
    });
}

function validateString(str) {
    const stringRegex = /^[a-zA-Z0-9!@#$%^&*()_+\-=\[\]{};:\\|,.<>\/?]+$/;
    return str.length <= 20 && stringRegex.test(str);
}

function validateForm() {
    const inputs = document.querySelectorAll('input[type="text"]');
    let isValid = true;

    inputs.forEach(input => {
        const name = input.name;
        const value = input.value;

        if (name.includes('ip')) {
            if (!validateIpAddress(value)) {
                alert(`Поле ${name} содержит некорректный IP-адрес.`);
                isValid = false;
            }
        } else {
            if (!validateString(value)) {
                alert(`Поле ${name} должно содержать не более 20 символов, только буквы, цифры и спецсимволы без пробелов и кавычек.`);
                isValid = false;
            }
        }
    });

    return isValid;
}

const form = document.querySelector('form');
if (form) {
    form.addEventListener('submit', (event) => {
        if (!validateForm()) {
            event.preventDefault();
        }
    });
}