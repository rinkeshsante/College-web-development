// toggle button
let button = document.querySelector(".btn-theme-toggle");
if (localStorage.clickcount % 2 == 0) {
  document.documentElement.classList.toggle("dark-mode");
}
button.addEventListener("click", () => {
  if (localStorage.clickcount) {
    localStorage.clickcount = Number(localStorage.clickcount) + 1;
  } else {
    localStorage.clickcount = 1;
  }
  document.documentElement.classList.toggle("dark-mode");
});

// for datatables
$(document).ready(function () {
  $("#dataTable").DataTable({
    initComplete: function () {
      this.api()
        .columns()
        .every(function () {
          var column = this;
          var select = $('<select><option value=""></option></select>')
            .appendTo($(column.footer()).empty())
            .on("change", function () {
              var val = $.fn.dataTable.util.escapeRegex($(this).val());

              column.search(val ? "^" + val + "$" : "", true, false).draw();
            });

          column
            .data()
            .unique()
            .sort()
            .each(function (d, j) {
              select.append('<option value="' + d + '">' + d + "</option>");
            });
        });
    },
  });
});
