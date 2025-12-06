import Link from 'next/link';
import { getSortedPostsData } from '@/lib/posts';

export default function Home() {
  const posts = getSortedPostsData();

  return (
    <main className="container">
      <header>
        <h1>Burhanuddin Pithawala</h1>
        <p>Notes on Growth and Marketing for Startups in India</p>
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
