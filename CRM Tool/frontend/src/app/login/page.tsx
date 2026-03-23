'use client';

import axios from 'axios';
import { useState } from 'react';
import { useRouter } from 'next/navigation';
import api from '@/lib/api';
import { Lock, User as UserIcon, AlertCircle, Loader2 } from 'lucide-react';

export default function LoginPage() {
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const [error, setError] = useState('');
    const [loading, setLoading] = useState(false);
    const router = useRouter();

    const handleLogin = async (e: React.FormEvent) => {
        e.preventDefault();
        setLoading(true);
        setError('');

        try {
            const formData = new URLSearchParams();
            formData.append('username', username);
            formData.append('password', password);

            const response = await api.post('/token', formData, {
                headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
            });

            localStorage.setItem('token', response.data.access_token);
            router.push('/dashboard');
        } catch (err: unknown) {
            if (axios.isAxiosError(err)) {
                setError(err.response?.data?.detail || 'Login failed. Please check your credentials.');
            } else {
                setError('Login failed. Please check your credentials.');
            }
        } finally {
            setLoading(false);
        }
    };

    return (
        <div className="min-h-screen flex items-center justify-center bg-slate-950 p-4">
            <div className="w-full max-w-md space-y-8 bg-slate-900 p-8 rounded-2xl border border-slate-800 shadow-2xl">
                <div className="text-center">
                    <div className="inline-flex items-center justify-center w-16 h-16 rounded-full bg-blue-500/10 mb-4 border border-blue-500/20">
                        <Lock className="w-8 h-8 text-blue-500" />
                    </div>
                    <h1 className="text-3xl font-bold tracking-tight text-white">CRM Secure Portal</h1>
                    <p className="mt-2 text-slate-400">Enter your credentials to access the system</p>
                </div>

                <form onSubmit={handleLogin} className="mt-8 space-y-6">
                    {error && (
                        <div className="flex items-center gap-2 p-4 text-sm text-red-400 bg-red-400/10 border border-red-400/20 rounded-lg animate-in fade-in duration-300">
                            <AlertCircle className="w-4 h-4 shrink-0" />
                            <p>{error}</p>
                        </div>
                    )}

                    <div className="space-y-4">
                        <div className="space-y-2">
                            <label className="text-sm font-medium text-slate-300 ml-1">Username</label>
                            <div className="relative group">
                                <UserIcon className="absolute left-3 top-1/2 -translate-y-1/2 w-5 h-5 text-slate-500 group-focus-within:text-blue-500 transition-colors" />
                                <input
                                    type="text"
                                    required
                                    value={username}
                                    onChange={(e) => setUsername(e.target.value)}
                                    className="w-full bg-slate-800 border border-slate-700 rounded-xl py-3 pl-11 pr-4 text-white placeholder-slate-500 focus:outline-none focus:ring-2 focus:ring-blue-500/50 focus:border-blue-500 transition-all"
                                    placeholder="admin"
                                />
                            </div>
                        </div>

                        <div className="space-y-2">
                            <label className="text-sm font-medium text-slate-300 ml-1">Password</label>
                            <div className="relative group">
                                <Lock className="absolute left-3 top-1/2 -translate-y-1/2 w-5 h-5 text-slate-500 group-focus-within:text-blue-500 transition-colors" />
                                <input
                                    type="password"
                                    required
                                    value={password}
                                    onChange={(e) => setPassword(e.target.value)}
                                    className="w-full bg-slate-800 border border-slate-700 rounded-xl py-3 pl-11 pr-4 text-white placeholder-slate-500 focus:outline-none focus:ring-2 focus:ring-blue-500/50 focus:border-blue-500 transition-all"
                                    placeholder="********"
                                />
                            </div>
                        </div>
                    </div>

                    <button
                        type="submit"
                        disabled={loading}
                        className="w-full py-3 px-4 bg-blue-600 hover:bg-blue-500 text-white font-semibold rounded-xl shadow-lg shadow-blue-500/20 flex items-center justify-center gap-2 transition-all disabled:opacity-70 disabled:cursor-not-allowed group"
                    >
                        {loading ? (
                            <Loader2 className="w-5 h-5 animate-spin" />
                        ) : (
                            'Sign In'
                        )}
                    </button>
                </form>

                <div className="pt-6 border-t border-slate-800 text-center">
                    <p className="text-slate-500 text-xs">
                        Security by Design Enforced | Unauthorized access is strictly prohibited
                    </p>
                </div>
            </div>
        </div>
    );
}
