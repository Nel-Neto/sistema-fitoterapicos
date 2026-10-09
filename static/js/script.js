document.addEventListener("DOMContentLoaded", () => {
    const search = document.querySelector('input[name="q"]');
    if (search && window.location.pathname === "/buscar") {
        search.focus();
    }
});
