import { useState, useEffect } from 'react';
import './App.css';
import { getUsersUsersGet, createUsersUsersPost } from './client';
import type { User } from './client';

function App() {
  const [users, setUsers] = useState<User[]>([]);
  const [name, setName] = useState('');
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [confirmPassword, setConfirmPassword] = useState('');

  const fetchUsers = async () => {
    const { data, error } = await getUsersUsersGet();
    if (error) {
      console.error(error);
    } else {
      console.log(data);
      setUsers(data!);
    }
  };

  useEffect(() => {
    fetchUsers();
  }, []);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    if (password !== confirmPassword) {
      alert("Passwords don't match");
      return;
    }
    const { error } = await createUsersUsersPost({
      body: { name, email, password, confirm_password: confirmPassword },
    });

    if (error) {
      console.error(error);
    } else {
      setName('');
      setEmail('');
      setPassword('');
      setConfirmPassword('');
      fetchUsers();
    }
  };

  return (
    <>
      <h1>Users</h1>
      <div className="card">
        {users.map((user) => (
          <div key={user.id}>
            <h2>{user.name}</h2>
            <p>{user.email}</p>
          </div>
        ))}
      </div>
      <div className="card">
        <h2>Create User</h2>
        <form onSubmit={handleSubmit}>
          <input
            type="text"
            placeholder="Name"
            value={name}
            onChange={(e) => setName(e.target.value)}
          />
          <input
            type="email"
            placeholder="Email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
          />
          <input
            type="password"
            placeholder="Password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
          />
          <input
            type="password"
            placeholder="Confirm Password"
            value={confirmPassword}
            onChange={(e) => setConfirmPassword(e.target.value)}
          />
          <button type="submit">Create</button>
        </form>
      </div>
    </>
  );
}

export default App
