import Link from 'next/link';
import { getSortedPostsData } from '@/lib/posts';

export default function Home() {
  const posts = getSortedPostsData();

  return (
    <main className="container">
      <header>
        <h1>Burhanuddin Pithawala</h1>
        <p className="intro">
          AI Leader & Growth Marketing Strategist. Currently heading AI Business at InterviewKickstart,
          transforming learning for thousands through AI-powered education. Ex Global Head of Marketing at OYO
          and Ex Growth Marketing Leader at HealthPlix. I help startups crack growth through data-driven marketing,
          product strategy, and AI transformation.
        </p>
        <p className="subtitle">Practical insights on growth, marketing analytics, and building scalable systems.</p>
      </header>

      <section className="posts">
        {posts.length === 0 ? (
          <p>No posts yet. Add markdown files to the posts directory.</p>
        ) : (
          <ul>
            {posts.map(({ slug, title, date }) => (
              <li key={slug}>
                <Link href={`/posts/${slug}`}>
                  {title}
                </Link>
                <small>{date}</small>
              </li>
            ))}
          </ul>
        )}
      </section>

      <footer>
        <p>Built with Next.js and Markdown</p>
      </footer>
    </main>
  );
}
