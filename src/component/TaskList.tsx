import { Component } from 'react';

interface Task {
  id: number;
  description: string;
  deadline: string;
  completed: boolean;
}

interface TaskListProps {
  tasks: Task[];
  onToggleComplete: (id: number) => void;
  onDeleteTask: (id: number) => void;
}

class TaskList extends Component<TaskListProps> {
  render() {
    const { tasks, onToggleComplete, onDeleteTask } = this.props;
    return (
      <ul>
        {tasks.map((task) => (
          <li key={task.id} style={{
            textDecoration: task.completed ? 'line-through' : 'none',
            color: task.completed ? 'gray' : 'black',
          }}>
            <span>{task.description} ({task.deadline})</span>
            <button onClick={() => onToggleComplete(task.id)}>
              {task.completed ? 'Bekor qilish' : 'Bajarildi'}
            </button>
            <button onClick={() => onDeleteTask(task.id)} style={{ marginLeft: '8px' }}>
              O‘chirish
            </button>
          </li>
        ))}
      </ul>
    );
  }
}

export default TaskList;
