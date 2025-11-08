// static/js/main.js

function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== "") {
    const cookies = document.cookie.split(";");
    for (let i = 0; i < cookies.length; i++) {
      const cookie = cookies[i].trim();
      if (cookie.substring(0, name.length + 1) === (name + "=")) {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}
const csrftoken = getCookie("csrftoken");

document.addEventListener("DOMContentLoaded", function() {
  document.querySelectorAll(".like-btn").forEach(btn => {
    btn.addEventListener("click", async function(e) {
      const postId = this.dataset.id;
      try {
        const res = await fetch(`/api/posts/${postId}/like/`, {
          method: "POST",
          headers: {
            "X-CSRFToken": csrftoken,
            "Accept": "application/json",
            "X-Requested-With": "XMLHttpRequest"
          },
          credentials: "same-origin"
        });
        if (!res.ok) throw new Error("Network error");
        const data = await res.json();
        this.querySelector(".like-count").innerText = data.like_count;
        if (data.liked) this.classList.add("btn-primary");
        else this.classList.remove("btn-primary");
      } catch (err) {
        console.error(err);
        window.location.href = `/like/${postId}/`;
      }
    });
  });
});
