function addTask() {
    var taskInput = document.getElementById('taskInput');
    var taskText = taskInput.value.trim();
  
    if (taskText !== '') {
      var taskList = document.getElementById('taskList');
      var newTask = document.createElement('li');
      newTask.innerHTML = taskText + ' <span class="close" onclick="removeTask(this)">×</span>';
      taskList.appendChild(newTask);
      taskInput.value = '';
    } else {
      alert('Please enter a task!');
    }
  }
  
  function removeTask(task) {
    task.parentNode.remove();
  }

  