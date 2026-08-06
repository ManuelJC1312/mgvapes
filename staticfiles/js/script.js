document.addEventListener("DOMContentLoaded", () => {

    // =====================================================================
    // MODAL DE CONTROL DE EDAD
    // =====================================================================
    const ageModal = document.getElementById("age-verification-modal");
    const btnYes = document.getElementById("btn-age-yes");
    const btnNo = document.getElementById("btn-age-no");

    if (ageModal) {
        const verified = sessionStorage.getItem("age-verified");
        if (!verified) {
            ageModal.style.display = "flex";
            document.body.classList.add("modal-open");
        }

        if (btnYes) {
            btnYes.addEventListener("click", () => {
                sessionStorage.setItem("age-verified", "true");
                ageModal.style.display = "none";
                document.body.classList.remove("modal-open");
            });
        }

        if (btnNo) {
            btnNo.addEventListener("click", () => {
                window.location.href = "https://www.google.com";
            });
        }
    }

    // =====================================================================
    // MODAL DE DETALLE DE PRODUCTOS (DINÁMICO)
    // =====================================================================
    const detailModal = document.getElementById("product-detail-modal");
    const closeModal = document.querySelector(".close-modal");

    if (detailModal) {
        document.querySelectorAll(".btn-detail-trigger").forEach(btn => {
            btn.addEventListener("click", () => {
                const card = btn.closest(".product-card");

                document.getElementById("modal-img").src =
                    card.querySelector(".product-img-container img").src;
                document.getElementById("modal-category").textContent =
                    card.querySelector(".product-category").textContent;
                document.getElementById("modal-title").textContent =
                    card.querySelector("h3").textContent;
                document.getElementById("modal-price").textContent =
                    card.querySelector(".product-price").textContent;
                document.getElementById("modal-desc").textContent =
                    card.dataset.desc || "";
                document.getElementById("modal-specs").textContent =
                    card.dataset.espec || "";

                const productName = card.querySelector("h3").textContent;
                const waBtn = document.getElementById("btn-modal-order");
                if (waBtn) {
                    waBtn.onclick = () => {
                        const msg = encodeURIComponent(`Hola, me interesa el producto: ${productName}`);
                        window.open(`https://wa.me/573000000000?text=${msg}`, "_blank");
                    };
                }

                detailModal.style.display = "flex";
                document.body.classList.add("modal-open");
            });
        });

        if (closeModal) {
            closeModal.addEventListener("click", () => {
                detailModal.style.display = "none";
                document.body.classList.remove("modal-open");
            });
        }

        window.addEventListener("click", (e) => {
            if (e.target === detailModal) {
                detailModal.style.display = "none";
                document.body.classList.remove("modal-open");
            }
        });
    }
});
