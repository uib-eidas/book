// mdBook: render ```mermaid blocks with the same Mermaid version as the slides.
(function() {
  document.querySelectorAll("code.language-mermaid").forEach(function(code) {
    var pre = document.createElement("pre");
    pre.className = "mermaid";
    pre.style.cssText = "background: none; font-family: Helvetica, Arial, sans-serif; text-align: center;";
    pre.textContent = code.textContent;
    code.parentNode.replaceWith(pre);
  });
  mermaid.initialize({ startOnLoad: false, theme: "base" });
  mermaid.init(undefined, ".mermaid");
})();
