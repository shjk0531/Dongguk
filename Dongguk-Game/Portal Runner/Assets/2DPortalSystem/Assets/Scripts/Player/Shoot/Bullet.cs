using UnityEngine;

public class Bullet : MonoBehaviour
{
    [SerializeField] private float _speed = 10f;

    [SerializeField] private Color OrangeColor;
    [SerializeField] private Color BlueColor;
    [SerializeField] private Color GrayColor;

    [HideInInspector] public float horizontalDirection;
    [HideInInspector] public float verticalDirection;
    [HideInInspector] private Color _teleportColor;
    private Rigidbody2D _r2d;
    private PortalSystem[] Teleports;

    public enum PortalColor
    {
        Orange = 1,
        Blue = 2
    }

    [HideInInspector] public PortalColor bulletType;

    void Start()
    {
        _r2d = gameObject.GetComponent<Rigidbody2D>();
        _r2d.velocity = new Vector2(horizontalDirection * _speed, verticalDirection * _speed);

        if (bulletType == PortalColor.Orange)
        {
            gameObject.GetComponent<SpriteRenderer>().color = OrangeColor;
            _teleportColor = OrangeColor;
        }
        else
        {
            gameObject.GetComponent<SpriteRenderer>().color = BlueColor;
            _teleportColor = BlueColor;
        }
    }

    private void OnTriggerEnter2D(Collider2D collision)
    {
        if (collision.gameObject.GetComponent<PortalDirection>())
        {
            SpawnTeleport(bulletType, _teleportColor, collision.gameObject);
            Destroy(gameObject);
        }
        else if(!collision.gameObject.GetComponent<CharacterController>()) {
            Destroy(gameObject);
        }
        
    }

    private void SpawnTeleport(PortalColor _tipeTeleport, Color BlockColor, GameObject _block)
    {
           
        if (_block.GetComponent<PortalDirection>())
            {
                Teleports = FindObjectsOfType<PortalSystem>();
                for (int i = 0; i < Teleports.Length; i++)
                {
                    if (Teleports[i].PortalType == (PortalSystem.PortalColor)_tipeTeleport)
                    {
                        if (!_block.GetComponent<PortalSystem>())
                        {
                            Destroy(Teleports[i].gameObject.GetComponent<PortalSystem>());
                            Teleports[i].gameObject.GetComponent<SpriteRenderer>().color = GrayColor;
                            Teleports[i].gameObject.tag = "Wall/Default";
                            Teleports[i].gameObject.GetComponent<Collider2D>().isTrigger = false;
                            Teleports[i].gameObject.transform.GetChild(0).gameObject.SetActive(false);
                    }
                    }
                }

                if (!_block.GetComponent<PortalSystem>())
                {
                    _block.AddComponent<PortalSystem>();
                    _block.GetComponent<PortalSystem>().PortalType = (PortalSystem.PortalColor)_tipeTeleport;
                    _block.GetComponent<SpriteRenderer>().color = BlockColor;
                    SetDirection(_block);       
                    _block.tag = "Wall/Teleport";
                    _block.transform.GetChild(0).gameObject.GetComponent<SpriteRenderer>().color = BlockColor;
                    GameObject[] ActiveTeleports = GameObject.FindGameObjectsWithTag("Wall/Teleport"); //GameObject.FindObjectsOfType<PortalSystem>()
                    if (ActiveTeleports.Length > 1)
                        for (int i = 0; i < ActiveTeleports.Length; i++)
                            ActiveTeleports[i].GetComponent<Collider2D>().isTrigger = true;
                }
            }
        
    }

    private void SetDirection(GameObject _portal)
    {
        _portal.GetComponent<PortalDirection>().horizontalDirection = (int)horizontalDirection;
        _portal.GetComponent<PortalDirection>().verticalDirection = (int)verticalDirection;
        _portal.GetComponent<PortalSystem>().DirrectionArrow(horizontalDirection, verticalDirection);
    }

}
