import { Component } from 'react';
import TaskForm from './TaskForm';
import TaskList from './TaskList';

interface Task {
  id: number;
  description: string;
  deadline: string;
  completed: boolean;
}

interface TaskManagerState {
  tasks: Task[];
}

class TaskManager extends Component<{}, TaskManagerState> {
  constructor(props: {}) {
    super(props);
    this.state = {
      tasks: [],
    };
  }

  componentDidMount() {
    const tasks = localStorage.getItem('tasks');
    if (tasks) {
      this.setState({ tasks: JSON.parse(tasks) });
    }
  }

  componentDidUpdate(prevState: TaskManagerState) {
    if (prevState.tasks !== this.state.tasks) {
      localStorage.setItem('tasks', JSON.stringify(this.state.tasks));
    }
  }

  addTask = (description: string, deadline: string) => {
    const newTask: Task = {
      id: Date.now(),
      description,
      deadline,
      completed: false,
    };
    this.setState((prevState) => ({
      tasks: [...prevState.tasks, newTask],
    }));
  };

  toggleComplete = (id: number) => {
    this.setState((prevState) => ({
      tasks: prevState.tasks.map((task) =>
        task.id === id ? { ...task, completed: !task.completed } : task
      ),
    }));
  };

  deleteTask = (id: number) => {
    this.setState((prevState) => ({
      tasks: prevState.tasks.filter((task) => task.id !== id),
    }));
  };

  render() {
    return (
      <div>
        <h2>Task Manager</h2>
        <TaskForm onAddTask={this.addTask} />
        <TaskList
          tasks={this.state.tasks}
          onToggleComplete={this.toggleComplete}
          onDeleteTask={this.deleteTask}
        />
      </div>
    );
  }
}

export default TaskManager;
