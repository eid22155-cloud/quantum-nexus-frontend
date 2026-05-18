import React, { useState } from 'react';

export default function QuantumNexusDashboard() {
  // 🌐 الرابط الموحد المباشر للسيرفر الخارجي على Railway الخاص بك
  const RAILWAY_SERVER_URL = "https://quantum-nexus-v10-production.up.railway.app"; 

  const [agentType, setAgentType] = useState('code');
  const [prompt, setPrompt] = useState('');
  const [response, setResponse] = useState('');
  const [telemetry, setTelemetry] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  const handleRunAgent = async (e) => {
    e.preventDefault();
    if (!prompt.trim()) return;

    setLoading(true);
    setError('');
    setResponse('');
    setTelemetry(null);

    try {
      const res = await fetch(`${RAILWAY_SERVER_URL}/api/agent/run`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          agent_type: agentType,
          prompt_used: prompt,
        }),
      });

      const data = await res.json();

      if (data.status === 'success') {
        setResponse(data.ai_response);
        setTelemetry(data.telemetry);
      } else {
        setError(data.message || 'حدث خطأ غير متوقع من خادم كوانتم.');
      }
    } catch (err) {
      setError('فشل الاتصال بالسيرفر السحابي. تأكد من أن سيرفر Railway يعمل بشكل صحيح.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div style={{ padding: '24px', maxWidth: '900px', margin: '0 auto', fontFamily: 'sans-serif', direction: 'rtl', backgroundColor: '#0b0f19', color: '#e2e8f0', minHeight: '100vh', borderRadius: '12px' }}>
      
      {/* الهيدر المركزي الخارق */}
      <header style={{ borderBottom: '1px solid #1e293b', paddingBottom: '16px', marginBottom: '24px', textAlign: 'center' }}>
        <h1 style={{ color: '#38bdf8', fontSize: '28px', margin: '0 0 8px 0' }}>🌌 Quantum Nexus OS - V10.3</h1>
        <p style={{ color: '#94a3b8', margin: 0 }}>نظام التحكم السحابي الموحد للأيرجنتات الذكية (Supabase Live Backend)</p>
      </header>

      {/* الفورم واختيار الأيجنت */}
      <form onSubmit={handleRunAgent} style={{ backgroundColor: '#1e293b', padding: '20px', borderRadius: '8px', marginBottom: '24px' }}>
        <div style={{ marginBottom: '16px' }}>
          <label style={{ display: 'block', marginBottom: '8px', fontWeight: 'bold', color: '#cbd5e1' }}>اختر الكيان الكمومي (Agent Type):</label>
          <select 
            value={agentType} 
            onChange={(e) => setAgentType(e.target.value)}
            style={{ width: '100%', padding: '10px', borderRadius: '6px', backgroundColor: '#0f172a', color: '#fff', border: '1px solid #475569', fontSize: '16px' }}
          >
            <option value="code"> Absolute Code Overlord (الأكواد والبرمجيات)</option>
            <option value="video"> Cinematic Director (السيناريو وإخراج الأفلام)</option>
            <option value="music"> Master AI Audio Composer (الموسيقى والهندسة الصوتية)</option>
            <option value="writing"> Infinite Knowledge Mind (الكتابة الإبداعية والبحوث)</option>
          </select>
        </div>

        <div style={{ marginBottom: '16px' }}>
          <label style={{ display: 'block', marginBottom: '8px', fontWeight: 'bold', color: '#cbd5e1' }}>اكتب برومبت العميل الرئيسي (Master Prompt):</label>
          <textarea
            rows="5"
            value={prompt}
            onChange={(e) => setPrompt(e.target.value)}
            placeholder="اكتب فكرتك هنا بالتفصيل ليقوم النظام بتحليلها وتشغيل الأيجنت المتخصص..."
            style={{ width: '100%', padding: '12px', borderRadius: '6px', backgroundColor: '#0f172a', color: '#fff', border: '1px solid #475569', fontSize: '15px', resize: 'vertical', boxSizing: 'border-box' }}
          />
        </div>

        <button 
          type="submit" 
          disabled={loading}
          style={{ width: '100%', padding: '12px', borderRadius: '6px', backgroundColor: loading ? '#64748b' : '#0284c7', color: '#fff', fontSize: '16px', fontWeight: 'bold', border: 'none', cursor: loading ? 'not-allowed' : 'pointer', transition: 'background-color 0.2s' }}
        >
          {loading ? '⚡ جاري استدعاء ومعالجة الذكاء الفائق...' : '🚀 إطلاق الأيجنت وتفعيل البروتوكول'}
        </button>
      </form>

      {/* شاشة عرض الأخطاء إن وجدت */}
      {error && (
        <div style={{ backgroundColor: '#7f1d1d', border: '1px solid #f87171', color: '#fca5a5', padding: '14px', borderRadius: '6px', marginBottom: '24px' }}>
          <strong>⚠️ تنبيه كوانتم:</strong> {error}
        </div>
      )}

      {/* لوحة قياسات الأداء السحابي (Telemetry) */}
      {telemetry && (
        <div style={{ backgroundColor: '#0f172a', border: '1px solid #38bdf8', padding: '14px', borderRadius: '6px', marginBottom: '24px', display: 'flex', justifyContent: 'space-between', flexWrap: 'wrap', fontSize: '14px' }}>
          <div>⏱️ زمن التنفيذ: <span style={{ color: '#38bdf8', fontWeight: 'bold' }}>{telemetry.execution_time_sec} ثانية</span></div>
          <div>⚡ السرعة: <span style={{ color: '#4ade80', fontWeight: 'bold' }}>{telemetry.tokens_per_second} Token/s</span></div>
          <div>☁️ حالة الاتصال: <span style={{ color: '#fbbf24', fontWeight: 'bold' }}>{telemetry.database_sync}</span></div>
        </div>
      )}

      {/* مستند مخرجات الأيجنت الخارق */}
      {response && (
        <div style={{ backgroundColor: '#0f172a', padding: '24px', borderRadius: '8px', border: '1px solid #334155', boxShadow: '0 4px 6px -1px rgba(0,0,0,0.5)' }}>
          <h2 style={{ color: '#4ade80', fontSize: '20px', marginTop: 0, marginBottom: '16px', borderBottom: '1px solid #334155', paddingBottom: '8px' }}>✨ المخرجات النهائية الفوق-ذكية:</h2>
          <div style={{ whiteSpace: 'pre-wrap', lineHeight: '1.7', color: '#cbd5e1', fontSize: '15px' }}>
            {response}
          </div>
        </div>
      )}

    </div>
  );
}
