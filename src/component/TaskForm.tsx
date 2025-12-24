import React, { Component } from 'react';

interface TaskFormProps {
  onAddTask: (description: string, deadline: string) => void;
}

interface TaskFormState {
  description: string;
  deadline: string;
  error: string;
}

class TaskForm extends Component<TaskFormProps, TaskFormState> {
  constructor(props: TaskFormProps) {
    super(props);
    this.state = {
      description: '',
      deadline: '',
      error: '',
    };
  }

  handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    this.setState({ [e.target.name]: e.target.value } as Pick<TaskFormState, keyof TaskFormState>);
  };

  handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    const { description, deadline } = this.state;
    if (!description.trim() || !deadline.trim()) {
      this.setState({ error: 'Iltimos, barcha maydonlarni to‘ldiring!' });
      return;
    }
    this.props.onAddTask(description, deadline);
    this.setState({ description: '', deadline: '', error: '' });
  };

  render() {
    return (
      <form onSubmit={this.handleSubmit}>
        <input
          type="text"
          name="description"
          placeholder="Vazifa tavsifi"
          value={this.state.description}
          onChange={this.handleChange}
        />
        <input
          type="date"
          name="deadline"
          value={this.state.deadline}
          onChange={this.handleChange}
        />
        <button type="submit">Qo‘shish</button>
        {this.state.error && <div style={{ color: 'red' }}>{this.state.error}</div>}
      </form>
    );
  }
}

export default TaskForm;
