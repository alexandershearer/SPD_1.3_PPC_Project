/* <script src="https://ajax.googleapis.com/ajax/libs/jquery/2.1.1/jquery.min.js"></script>
<form>
  <div id="workouts">
    <div class="workout" id="workout1">
      <label>Workout:</label>
      <input type="text">
    </div>
  </div>

  <button id="addWorkout" type="button">Add</button>
</form> */
function addForm(e) {
    e.preventDefault();
    var last = (".eventsChart").last().attr("class")
    template = "<div class='eventForm' id='eventForm" + parseInt(last[-1])+1 + "'>{% include 'form.html' %}"
    (".eventsChart").append(template);
}